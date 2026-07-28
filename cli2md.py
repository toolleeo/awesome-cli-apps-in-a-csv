import csv
import json
import string
import re



summary_template = """
Summary:

* Apps/tools: **{n_apps}**
* Categories: **{n_cats}**

# Contents

{cats}
"""

resources_template = """
# <a name="resources"></a>Related resources

A list of some online resources that contribute interesting links to apps and info.

{}
"""


def load_csv(file_name):
    with open(file_name, 'r') as infile:
        csv_reader = csv.DictReader(infile, delimiter=',')
        fields = csv_reader.fieldnames
        data = []
        for item in csv_reader:
            data.append(item)
    return fields, data


def fmt_app(app):
    descr = ''.join(c if c != '\n' else ' ' for c in app['description'])
    if app['homepage'] != '':
        st = '* [{}]({}) - {}'.format(app['name'], app['homepage'], descr)
    elif app['git'] != '':
        st = '* [{}]({}) - {}'.format(app['name'], app['git'], descr)
    else:
        st = '* {} - {}'.format(app['name'], descr)
    return st


def print_grouped_apps(groups, cats, apps):
    for group in groups:
        label = group.replace(' ', '-')
        print(f'# <a name="{label}"></a>{group}\n')
        for c in groups[group]:
            cat_item = cats[c]
            print('## <a name="{}"></a>{}\n'.format(c, cat_item['name']))
            if cat_item['description'] != '':
                print(f"{cat_item['description']}.\n")
            apps_in_cat = [a for a in apps if a['category'] == c]
            apps_in_cat = sorted(apps_in_cat, key=lambda i: i['name'].upper())
            for app in apps_in_cat:
                print(fmt_app(app))
            print()


def print_apps(cats, apps):
    """Old formatting with categories sorted by name."""
    for c in cats:
        cat_item = cats[c]
        print('## <a name="{}"></a>{}\n'.format(c, cat_item['name']))
        if cat_item['description'] != '':
            print(f"{cat_item['description']}.\n")
        apps_in_cat = [a for a in apps if a['category'] == c]
        apps_in_cat = sorted(apps_in_cat, key=lambda i: i['name'].upper())
        for app in apps_in_cat:
            print(fmt_app(app))
        print()


def github_slug(text):
    # 1. Lowercase
    slug = text.lower()
    # 2. Remove anything that's not a word char, space, or hyphen
    slug = re.sub(r'[^\w\s-]', '', slug)
    # 3. Replace spaces with dashes
    slug = re.sub(r'\s+', '-', slug)
    return slug


def fmt_grouped_categories(cats, groups):
    lines = []
    for group in groups:
        label = github_slug(group)
        lines.append(f'## [{group}](#{label}-1)')
        for c in groups[group]:
            lines.append(f"* [{cats[c]['name']}](#{c}) ({cats[c]['count']})")
    return '\n'.join(lines)


def fmt_categories(cats):
    """Old formatting with categories sorted by name and grouped in one line per letter."""
    group_by_letters = {x: [] for x in string.ascii_uppercase}
    for c in cats:
        initial = cats[c]['name'][0].upper()
        group_by_letters[initial].append(c)
    # print(group_by_letters)
    strings_by_letters = {x: [] for x in string.ascii_uppercase}
    for g in group_by_letters:
        strings_by_letters[g] = [f"[{cats[c]['name']}](#{c}) ({cats[c]['count']})" for c in group_by_letters[g]]
    lines_by_letters = {x: [] for x in string.ascii_uppercase}
    # print(strings_by_letters)
    for g in group_by_letters:
        lines_by_letters[g] = ', '.join(strings_by_letters[g])
    lines_to_join = ['* ' + lines_by_letters[key] for key in lines_by_letters if len(lines_by_letters[key])]
    # print(lines_by_letters)
    # print(lines_to_join)
    return '\n'.join(lines_to_join)


def count_apps(apps, categories):
    for c in categories:
        categories[c]['count'] = 0
    for a in apps:
        c = a['category']
        if c in categories:
            categories[c]['count'] += 1
        # else:
        #     print('Category {} does not have any app'.format(c))
    return categories


def categories_list_to_dict(category_list):
    category_list = sorted(category_list, key=lambda d: d['name'])
    d = {}
    for c in category_list:
        d[c['label']] = {'name': c['name'], 'description': c['description']}
    return d


def main():
    _, apps = load_csv('data/apps.csv')
    _, categories = load_csv('data/categories.csv')
    _, resources = load_csv('data/resources.csv')
    with open('data/groups.json', 'r') as f:
        groups = json.load(f)
    categories = categories_list_to_dict(categories)
    categories = count_apps(apps, categories)

    md_res = ''
    for r in resources:
        md_res += '[{}]({}) - {}\n\n'.format(r['title'], r['url'], r['description'])

    print(summary_template.format(n_apps=len(apps), n_cats=len(categories), cats=fmt_grouped_categories(categories, groups)))
    print_grouped_apps(groups, categories, apps)
    print(resources_template.format(md_res))


if __name__ == '__main__':
    main()
