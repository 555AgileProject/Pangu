import Project03 as p3

def test_case():
    path = '/Users/qizhao/Documents/TeamDemo/proj02test.ged'
    path2 = '/Users/qizhao/Documents/Spring 2020/555/qzhao_testfile.ged'
    test_repo = p3.Repository(path2)
    test_repo._analyze_files()
    test_repo.pretty_print()

if __name__ == '__main__':
    test_case()