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
class TreeFloat:
        def CreateTree(self):
                alphabets=[
                        Node(20,alphabet.Alphabet().AlphabetNumber()),
                        Node(10,['=']),
                        Node(22,[' ']),
                        Node(5,alphabet.Alphabet().GenerateLetters()),
                        Node(11,[' ']),
                        Node(4,['i','n','t']),
                        Node(8,[' '])
                        ]
                tree=Tree.Tree()
                for x in alphabets:
                        tree.root=tree.insert(tree.root,x.value,x.alphabet)
                return tree

#creating the first tree
thunk=TreeFloat().CreateTree()
thunk.PostOrder(thunk.root,ConvertString.ConvertString('float d=10').Convert())
