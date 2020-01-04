import falcon as F
import os

class PageResource(object):
	def on_get(self, req, resp):
		resp.content_type="text/html"
		with open("FalconWebAPI-UTx10101/views/index.html",'r') as f:
			resp.body = f.read()
		resp.status = F.HTTP_200

class Img(object):
	def on_get(self, req, resp, fname):
		resp.content_type="image/"+[fname.split(".")[-1],"svg+xml"][fname.split(".")[-1]=="svg"]
		img_path = os.path.join("FalconWebAPI-UTx10101/views/images", fname)
		resp.stream =  open(img_path,"rb")
		resp.stream_len = os.path.getsize(img_path)

application = api = F.API()
api.add_route('/', PageResource())
api.add_route('/images/{fname}', Img())
