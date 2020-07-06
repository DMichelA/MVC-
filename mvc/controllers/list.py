import web

render = web.template.render("mvc/views/")

class List():

    def GET(self):
        try:
            return render.list() # renderizando list.html
        except Exception as e:
            return "Error " + str(e.args)