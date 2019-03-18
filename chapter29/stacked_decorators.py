# Define the decorator functions
def make_bold(fn):
    def makebold_wrapped():
        return "<b>" + fn() + "</b>"

    return makebold_wrapped


def make_italic(fn):
    def makeitalic_wrapped():
        return "<i>" + fn() + "</i>"

    return makeitalic_wrapped


# Apply decorators to function hello
@make_bold
@make_italic
def hello():
    return 'hello world'


# Call function hello 
print(hello())
