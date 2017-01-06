# bristol_project
Final Day Project at Bristol Intermediate Software Carpentry Course

##Order of processes:

1. Create 1st referencing set from manually collected reference images (e.g. bristol_reference_1.png)
2. Create segment dictionary of original image
3. Search segment dictionary with pixel values from 1st reference set
4. Select segments that meet a threshold of matching pixel values
5. Create 2nd referencing set from the pixels within the selected segments
6. Repeat steps 3, 4, & 5 until an acceptable set of segments have been defined as trees
7. Run pixel_search.py for final reference set
8. Create final image
