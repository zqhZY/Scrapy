BOT_NAME = 'sql_test'

SPIDER_MODULES = ['sql_test.spiders']
NEWSPIDER_MODULE = 'sql_test.spiders'
ITEM_PIPELINES = {'sql_test.pipelines.SqlTestPipeline' : 301}

