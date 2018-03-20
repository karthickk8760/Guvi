def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or ' ' for x in word.split(' '))
a=raw_input()
print(snake_to_camel(a))
