# ManagedMenuPopupItem

Managed MenuPopupItem.
 
Extends <link displaytype="text" defaultstyle="true" type="topiclink" href="ManagedObject" styleclass="Normal" translate="true">ManagedObject</link>.

Extends SeSSimulatedObject.





**Behavior Pattern: ManagedMenuItemBehavior**


<!-- ============================== property summary ========================== -->

	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[DoMenu](#DoMenu) | Performs click on the menu item. |




<!-- ============================== property detail ========================== -->
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="DoMenu"></a>    
#### DoMenu(path, separator)

Performs click on the menu item.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| path | string |	Path from the menu root to a leaf item with components delimited by separator parameter. |
| separator | string |	Separator character.<br>Optional, Default: ;. |




**Returns:**

boolean: 'true' if success, 'false' otherwise.



<a name="see.also.managedmenupopupitem.domenu"></a>

	
