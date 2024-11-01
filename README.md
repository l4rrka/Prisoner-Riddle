100 Prisoners Problem

The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains 100 numbered boxes. The director randomly puts one prisoner's number in each closed box. The prisoners enter the room, one after another. Each prisoner may open and look into 50 boxes in any order. The boxes are closed again afterwards. If, during this search, every prisoner finds their number in one of the boxes, all prisoners are pardoned. If even one prisoner does not find their number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first prisoner enters to look in the boxes. What is the prisoners' best strategy?

Solution:
1.	Each prisoner first opens the drawer labelled with their own number.
2.	If this drawer contains their number, they are done and were successful.
3.	Otherwise, the drawer contains the number of another prisoner, and they next open the drawer labelled with this number.
4.	The prisoner repeats steps 2 and 3 until they find their own number, or fail because the number is not found in the first fifty opened drawers.
This increases their total chance of success to ~31%.

