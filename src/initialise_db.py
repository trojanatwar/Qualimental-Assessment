import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from .model import (
    DBSession,
    Page,
    Base,
    User
    )

from tqdm import tqdm

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    with transaction.manager:

        for user_id in [1,2,3,4,5]:
            umodel = User(name=f"user"+str(user_id))
            DBSession.add(umodel)    

            # For each user create 1,000,000 entries
            for i in tqdm(range(10000)):
                model = Page(title='Root', body='<p>Root</p>', owner=umodel)
                DBSession.add(model)