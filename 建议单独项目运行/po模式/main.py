import unittest


if __name__ == '__main__':
    # 收集用例
    suite = unittest.defaultTestLoader.discover("../../下载/po模式/scripts")

    # 运行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
