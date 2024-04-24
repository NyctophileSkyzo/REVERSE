class hello:
    def print_hello(self):
        print("""
  Source Obfuscated with Chimera
       The lost Source - KEY

""")
    
if __name__ == '__main__':
    obj = hello()
    from os import system as automation ; import sys
    automation('clear' if 'linux' in sys.platform.lower() else 'cls')
    obj.print_hello()
