import web

render = web.template.render("mvc/views/")

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando insert.html
        except Exception as e:
            return "Error " + str(e.args)