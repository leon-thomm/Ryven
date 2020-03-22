class GlobalStorage:
    storage = {'design style': 'dark std',
               'debugging': False}

    def debug(*args):
        s = ''
        for arg in args:
            s += ' '+str(arg)
        if GlobalStorage.storage['debugging']:
            print('        --> DEBUG:', s)

    # yyep, that's it....
    # you must be kidding...
    # you MUST be
    # it's actually true....
    # that's ridiculous.
    # indeed.
