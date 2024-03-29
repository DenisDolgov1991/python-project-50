ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
NESTED = 'nested'
UPDATED = 'updated'


def build_diff_tree(content1, content2):
    diff_tree = {}
    all_keys = content1.keys() | content2.keys()
    added = content2.keys() - content1.keys()
    deleted = content1.keys() - content2.keys()

    for key in sorted(all_keys):
        if key in added:
            diff_tree[key] = {
                'status': ADDED,
                'value': content2.get(key)
            }
        elif key in deleted:
            diff_tree[key] = {
                'status': DELETED,
                'value': content1.get(key)
            }
        elif content1.get(key) == content2.get(key):
            diff_tree[key] = {
                'status': UNCHANGED,
                'value': content1.get(key)
            }
        elif isinstance(content1.get(key), dict) \
                and isinstance(content2.get(key), dict):
            diff_tree[key] = {
                'status': NESTED,
                'value': build_diff_tree(content1.get(key), content2.get(key))
            }
        else:
            diff_tree[key] = {
                'status': UPDATED,
                'value': [content1.get(key), content2.get(key)]
            }

    return diff_tree
