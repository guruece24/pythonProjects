import sys
print(sys.version)
print(sys.argv)
print(sys.orig_argv)


sys.argv[0] = "karthik" """
sys.argv[2] = "the legend"
***"""
x =  "hello".join(sys.argv[1:])
print(x)

print(len(sys.argv))
for n in sys.argv:
   print( "\n".join(sys.argv[1:]))

#sys.exit("failed")

print(f"type whatever you want")
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}. Type q to exit')
print("Exit")

sys.stdout.write('Geeks')

"""def fun(*args):
    print(args[0], file=sys.stderr)

fun("Hello World") """

print(sys.modules)
