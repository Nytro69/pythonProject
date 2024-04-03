from tree import Tree

tree = Tree(3,
            Tree(5,
                 Tree(15),
                 Tree(25)),
            Tree(7,
                 Tree(17),
                 Tree(27,
                      Tree(217),
                      Tree(228)))
            )


print(tree.height())