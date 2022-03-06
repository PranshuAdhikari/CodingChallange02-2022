import pandas as pd
from utils import *
from db_store import *

df = pd.read_csv('commoncrawl_lookup.csv')

pd.options.display.max_columns = None
pd.options.display.max_rows = None

for index, row in df.iterrows():

    print(row)

    try:

        url = row['url']
        html = load_single_warc_record(row['source_url'], row['source_offset'], row['source_offset'])

        nodes = str(list(get_node_tags(get_nodes(html))))
        left_sibling_tags = str(list(get_left_sibling_tags(get_nodes(html))))
        right_sibling_tags = str(list(get_right_sibling_tags(get_nodes(html))))
        parent_tags = str(list(get_parent_tags(get_nodes(html))))

        # data insertion
        insert_data(url, html, nodes, parent_tags, left_sibling_tags, right_sibling_tags)

    except Exception as ex:
        print('Exception :: ', ex)


