from retrieve_dependency import make_miz_dependency
from create_graph import create_graph
from pagerank import calc_pagerank
from hits import calc_hits
from create_table import create_table
from calc_pagerank_minus_hits import calc_pagerank_minus_hits
import sys

if __name__ == '__main__':
    mml_version = sys.argv[1]
    print("create graph")
    article2ref_articles = make_miz_dependency(mml_version)
    create_graph(article2ref_articles, mml_version)
    print("calculate PageRank")
    calc_pagerank(mml_version)
    print("calculate HITS")
    calc_hits(mml_version,auth=True)
    calc_hits(mml_version,auth=False)
    print("create HITS(auth)-PageRank table")
    create_table(mml_version=mml_version)
    print("Calculate (PageRank Score) - (HITS Authority Score)")
    calc_pagerank_minus_hits(mml_version)