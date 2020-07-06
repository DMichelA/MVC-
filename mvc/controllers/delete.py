import web

render = web.template.render("mvc/views/")

class Delete():

    def GET(self):
        try:
            return render.delete() # renderizando delete.html
        except Exception as e:
            return "Error " + str(e.args)