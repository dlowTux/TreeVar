import Tree
import alphabet
import ConvertString
#int v=10
#int v =10
#int v = 10
class Node:
        def __init__(self,value,alphabet):
                self.value=value
                self.alphabet=alphabet
class TreeString:
      
        def CreateTree(self):
                alphabets=[
                        Node(20,alphabet.Alphabet().LetterWithSimbols()),
                        Node(10,['=']),
                        Node(22,[' ']),
                        Node(5,alphabet.Alphabet().GenerateLetters()),
                        Node(11,[' ']),
                        Node(4,['S','t','r','i','n','g']),
                        Node(8,[' '])
                        ]
                tree=Tree.Tree()
                for x in alphabets:
                        tree.root=tree.insert(tree.root,x.value,x.alphabet)
                return tree

#creating the first tree
thunk=TreeString().CreateTree()
thunk.PostOrder(thunk.root,ConvertString.ConvertString('String hola').Convert())

