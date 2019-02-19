---
layout: post
title: Pascal trees for range searching
date: 2017-07-02 15:45
---
Let's try the same Pascal's triangle trick that we used in the last post to make [point sets with no large convex polygon]({{site.baseurl}}{% post_url 2017-07-01-pascals-triangle-points %}), on a different kind of object.
Instead of point sets, we'll make binary search trees.

Form a family of binary trees with $$\tbinom{n}{i}$$ leaves, as follows.

* When $$i=0$$ or $$i=n,$$ then $$\tbinom{n}{i}=1$$ and there is only one tree node.

* For any other choice of $$i,$$ use the tree for $$\tbinom{n-1}{i-1}$$ as the left subtree and the tree for $$\tbinom{n-1}{i}$$ as the right subtree, with an additional node as their parent.

Like this:

{: style="text-align:center"}
![32-vertex Pascal's triangle of binary search trees]({{site.baseurl}}/assets/2017/pascal-trees.svg)

And again, let's take the trees on a single row, and connect them together with the same gluing operation (a new node with a left and right subtree) in left-to-right order, so that their number of leaves is a power of two
(and their number of nodes is one less than a power of two):

{: style="text-align:center"}
![32-vertex Binary search trees constructed from whole rows of Pascal's triangle]({{site.baseurl}}/assets/2017/pow2-trees.svg)

Why?

Well, here's one possible answer. You may know that one application of binary search trees is in handling range search queries. Suppose you have a data set organized as a binary search tree and you want to know something about the subset of the data in a range $$[L,R].$$ Then you can do a binary search for $$L$$ and $$R,$$ and find the subset you want as individual nodes on the two search paths plus whole subtrees between the two paths. In the illustration below I've marked the roots of the whole subtrees in yellow. (The leaf at the far right of the blue range is on the search path, so it doesn't count as a whole subtree; the yellow subtree roots are children of search path nodes but not on the search path themselves.)

{: style="text-align:center"}
![32-vertex Range search in a binary tree]({{site.baseurl}}/assets/2017/range-search.svg)

You might think that a complete binary tree, like the one above, would be the best choice for this search, but it might not be. In range searching queries like this, it's often the case that the subtrees between the search paths are more expensive than the individual nodes on the paths. This is because you might have to do another query (say, a range search in another dimension) on those subtrees, whereas that same information can be computed directly for a single node. So, the goal should be to minimize the number of subtrees on your paths.

In a complete binary search tree with $$2^n-1$$ nodes, such as the one shown above for $$n=6,$$ you can find ranges that put as many as $$2n-4$$ complete subtrees inside the range: for instance, consider a range that excludes only the first and last leaf nodes of the tree. In contrast, the binary search tree formed from row $$n-1$$ of the Pascal triangle of trees has exactly the same number of nodes, but every range contains at most $$n-2$$ complete subtrees. That is, for range search problems where the interior subtrees are the most expensive part of the search, these Pascal trees are twice as efficient.
The analysis proving this property is more or less the same as the analysis for convex polygons in point sets, but with the subtrees on the left and right sides of a search path replacing caps and cups respectively.

You pay for this by having deeper search paths, though, so this only works when the complete subtrees are the expensive part of the search. An alternative possibility would be to use a shallower and more balanced tree to link up the subtrees from a row of the triangle, making the search depth only $$\log_2 n+O(\log\log n)$$ but possibly increasing the number of complete subtrees per search by that same $$O(\log\log n)$$ term.