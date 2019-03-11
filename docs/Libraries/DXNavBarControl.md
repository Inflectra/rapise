# DXNavBarControl

DevXpress NavBar.
 
Extends ManagedObject.

Extends SeSSimulatedObject.





**Behavior Pattern: DXNavBarControlBehavior**


<!-- ============================== property summary ========================== -->

	

### Property Summary

| **Property** | **Description** | **Getter** | **Setter** |
| ------------ | --------------- | ---------- | ---------- |
| [Item](#Item) | Caption of the item specified by index | GetItem |  |
| [ItemCount](#ItemCount) | Number of items. | GetItemCount |  |



	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[DoClickItem](#DoClickItem) | Performs click on the navigation item |
|	[DoExpandGroup](#DoExpandGroup) | Expand (or make active) the navigation group |




<!-- ============================== property detail ========================== -->
	
### Property Detail
		
<a name="Item"></a>
#### Item


Caption of the item specified by index

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| ind | number | Index of an item to get caption |


	
			
Type: string
			
			
Accessors: GetItem
			
		
<a name="ItemCount"></a>
#### ItemCount


Number of items.

			
	
			
Type: number
			
			
Accessors: GetItemCount
			
		
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="DoClickItem"></a>    
#### DoClickItem(nameCaptionIndex)

Performs click on the navigation item


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| nameCaptionIndex | string \| number |	index, name or caption of the item to be selected. |




**Returns:**

boolean: 'true' if successful, 'false' otherwise.



<a name="see.also.dxnavbarcontrol.doclickitem"></a>

<a name="DoExpandGroup"></a>    
#### DoExpandGroup(nameCaptionIndex)

Expand (or make active) the navigation group


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| nameCaptionIndex | string \| number |	index, name or caption of the item to be selected. |




**Returns:**

boolean: 'true' if successful, 'false' otherwise.



<a name="see.also.dxnavbarcontrol.doexpandgroup"></a>

	
