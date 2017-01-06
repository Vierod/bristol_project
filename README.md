# bristol_project
Final Day Project at Bristol Intermediate Software Carpentry Course

###
Order of processes:
> Create 1st referencing set from manually collected reference images (e.g. bristol_reference_1.png)
> Create segment dictionary of original image
> Search segment dictionary with pixel values from 1st reference set
> Select segments that meet a threshold of matching pixel values
> Create 2nd referencing set from the pixels within the selected segments
> Repeat steps 3, 4, & 5 until an acceptable set of segments have been defined as trees
> Run pixel_search.py for final reference set
> Create final image
