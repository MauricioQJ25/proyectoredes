#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'FJsJbyQOnK7Z06OwyWcXkoGbI'
CONSUMER_SECRET = 'AP8ElOgND8VBwEcjGlyAw14nJX9qDTnIjvK5JCFpLMxZt0CAqi'
ACCESS_KEY = '116272725-8BjUdjcUMgaT5Fw7THCoboK8sPYTe1jPW1xLtY1C'
ACCESS_SECRET = 'fnSxdpabFZqaCFtWMETJ78jqdJJkmZZxtotgbQkGvwXoq'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
