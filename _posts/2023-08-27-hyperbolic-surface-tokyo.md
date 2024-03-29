---
layout: post
title: A hyperbolic surface in Tokyo
date: 2023-08-27 16:51
---
_Sundial_, a 2018 sculpture by [Hiroshi Sugimoto](https://en.wikipedia.org/wiki/Hiroshi_Sugimoto), stands at the corner of a busy intersection in [Ōtemachi](https://en.wikipedia.org/wiki/%C5%8Ctemachi), a skyscraper district near downtown Tokyo. Despite this prominent location, it might easily be missed by passers-by whose attention is instead caught by a bright red agglomeration of steel tubes across the street. But of the two artworks, Sugimoto's is by far the more interesting from the mathematical point of view.

{: style="text-align:center"}
![Sundial, Hiroshi Sugimoto, 2018, Otemachi Place, Tokyo, looking south](https://www.ics.uci.edu/~eppstein/pix/sugsun/LookingSouth-m.jpg){: style="border-style:solid;border-color:black" }

As Sugimoto has [stated more explicitly for some of his related works](https://www.sugimotohiroshi.com/site-specific-arts), this sculpture appears to have a shape called the [pseudosphere](https://en.wikipedia.org/wiki/Pseudosphere) or tractroid. Mathematically, the pseudosphere extends infinitely far in the vertical direction, and has a horizontally-reflected copy that extends downward with the same shape, but for practical reasons it has been truncated here. The pseudosphere resembles a different shape called [Gabriel's horn](https://en.wikipedia.org/wiki/Gabriel's_horn), but Gabriel's horn is an algebraic surface whereas the pseudosphere is transcendental: it cannot be expressed as the solution to a polynomial equation. Gabriel's horn has finite volume but infinite surface area; in contrast, the pseudosphere has finite values for both its volume and surface area. Gabriel's horn is usually depicted truncated at its flared trumpet end (at height one, when oriented vertically as in Sugimoto's sculpture) but if extended downward toward the <span style="white-space:nowrap">$$xy$$-plane</span> it would spread out towards infinity, becoming arbitrarily flat but never reaching the plane. Instead, the pseudosphere flares more suddenly to meet its horizontal tangent plane in a finite circle.

The pseudosphere is of interest mathematically for the fact that its [Gaussian curvature](https://en.wikipedia.org/wiki/Gaussian_curvature) is the same at all points. 
This is true also for a sphere or a flat plane, but they have uniformly positive or zero curvature. The pseudosphere has uniformly negative curvature, like a saddle. The curvature of a sphere is the inverse of its radius, and the curvature of any other surface can be expressed as the product of the curvatures of two spheres, approximating its shape in two perpendicular directions. You can imagine one of these spheres hidden inside the spire of the sculpture, touching it from the inside in a horizonal circle, and the other one outside it, rolling around the sculpture on the same circle. As you go higher on the sculpture, the inside sphere becomes smaller but the outside sphere becomes larger; these effects cancel so that the product of the two spheres' curvatures remains unchanged.

If you had a sheet of hyperbolic paper of the same curvature, you could spread it out anywhere on the surface of the sculpture and it would conform perfectly to that surface, perhaps overlapping itself if you placed the paper high on the sculpture where it thins to a narrow spire. That is, locally this surface is a model of the [hyperbolic plane](https://en.wikipedia.org/wiki/Hyperbolic_geometry). The hyperbolic plane itself cannot be embedded into 3d without distorting its geometry or making it infinitely ruffly, and the pseudosphere fails to be an embedding in two ways: you can find short but uncontractable loops on its surface (tie a ribbon around the sculpture) and it has a boundary (the bottom rim of the sculpture). But in a local neighborhood around each point, measuring distances and angles on its surface, it has the same geometry as the hyperbolic plane.

Sugimoto is a photographer as well as a sculptor, famous for his blurred architectural abstractions. I could not resist taking one myself, of the skyscrapers of Otemachi, seen reflected in the surface of Sugimoto's _Sundial_:

{: style="text-align:center"}
![The skyscrapers of Otemachi reflected in Hiroshi Sugimoto's sculpture Sundial (2018)](https://www.ics.uci.edu/~eppstein/pix/sugsun/ReflectedSkyscrapers-m.jpg){: style="border-style:solid;border-color:black" }

If you're not in Japan, another similar sculpture by Sugimoto, _Point of Infinity_, has [recently been installed](https://www.archpaper.com/2023/06/hiroshi-sugimotos-point-of-infinity-installed-yerba-buena-island/) in a park on Yerba Buena island, near San Francisco.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/110964305525128696))