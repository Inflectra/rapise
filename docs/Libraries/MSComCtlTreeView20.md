# MSComCtlTreeView20

Extends [ActiveXObject](ActiveXObject.md)

Extends [SeSSimulatedObject](SeSSimulatedObject.md)





**Behavior Pattern: MSComCtlTreeView20Behavior**


<!-- ============================== property summary ========================== -->

	

### Property Summary

| **Property** | **Description** | **Getter** | **Setter** |
| ------------ | --------------- | ---------- | ---------- |
| [Checked](#Checked) | Checked state of the selected node or a node specified by the input parameters. | GetChecked |  |
| [ChildrenCount](#ChildrenCount) | Number of children of the selected node or a node specified by the input parameters. | GetChildrenCount |  |
| [Expanded](#Expanded) | Expanded state of the selected node or a node specified by the input parameters. | GetExpanded |  |
| [IndexPath](#IndexPath) | Index path of the specified or selected tree node i.e. | GetIndexPath |  |
| [NodeText](#NodeText) | Text of the selected node or a node specified by the input parameters. | GetNodeText |  |
| [Selected](#Selected) | Selected state of the selected node or a node specified by the input parameters | GetSelected |  |
| [Text](#Text) | ;-combined text of all selected nodes. | GetText |  |



	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[DoClickNode](#DoClickNode) | Clicks specific node in the tree. |
|	[DoCollapse](#DoCollapse) | Collapses specific node in the tree. |
|	[DoExpand](#DoExpand) | Expands specific node in the tree. |
|	[DoSetCheck](#DoSetCheck) | Set 'checked' state of the specified node |




<!-- ============================== property detail ========================== -->
	
### Property Detail
		
<a name="Checked"></a>
#### Checked


Checked state of the selected node or a node specified by the input parameters.

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| path | string | Path of the node |
| separator | string | Separator character.<br>Optional, Default: ;. |
| pathType | string | Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |


	
			
Type: boolean
			
			
Accessors: GetChecked
			
		
<a name="ChildrenCount"></a>
#### ChildrenCount


Number of children of the selected node or a node specified by the input parameters.

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| path | string | Path of the node |
| separator | string | Separator character.<br>Optional, Default: ;. |
| pathType | string | Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |


	
			
Type: string|boolean
			
			
Accessors: GetChildrenCount
			
		
<a name="Expanded"></a>
#### Expanded


Expanded state of the selected node or a node specified by the input parameters.

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| path | string | Path of the node |
| separator | string | Separator character.<br>Optional, Default: ;. |
| pathType | string | Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |


	
			
Type: boolean
			
			
Accessors: GetExpanded
			
		
<a name="IndexPath"></a>
#### IndexPath


Index path of the specified or selected tree node i.e. string in form '0;5;2;1;6', 'false' if fails

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| path | string | Path of the node |
| separator | string | Separator character.<br>Optional, Default: ;. |
| pathType | string | Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |


	
			
Type: string|boolean
			
			
Accessors: GetIndexPath
			
		
<a name="NodeText"></a>
#### NodeText


Text of the selected node or a node specified by the input parameters.

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| path | string | Path of the node |
| separator | string | Separator character.<br>Optional, Default: ;. |
| pathType | string | Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |


	
			
Type: string|boolean
			
			
Accessors: GetNodeText
			
		
<a name="Selected"></a>
#### Selected


Selected state of the selected node or a node specified by the input parameters

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| path | string | Path of the node |
| separator | string | Separator character.<br>Optional, Default: ;. |
| pathType | string | Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |


	
			
Type: boolean
			
			
Accessors: GetSelected
			
		
<a name="Text"></a>
#### Text


;-combined text of all selected nodes.

			
	
			
Type: string
			
			
Accessors: GetText
			
		
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="DoClickNode"></a>    
#### DoClickNode(path, separator, pathType)

Clicks specific node in the tree.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| path | string |	Path of the node |
| separator | string |	Separator character.<br>Optional, Default: ;. |
| pathType | string |	Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |




**Returns:**

boolean: 'true' if success, 'false' otherwise.



<a name="see.also.mscomctltreeview20.doclicknode"></a>

<a name="DoCollapse"></a>    
#### DoCollapse(path, separator, pathType)

Collapses specific node in the tree.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| path | string |	Path of the node |
| separator | string |	Separator character.<br>Optional, Default: ;. |
| pathType | string |	Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |




**Returns:**

boolean: 'true' if success, 'false' otherwise.



<a name="see.also.mscomctltreeview20.docollapse"></a>

<a name="DoExpand"></a>    
#### DoExpand(path, separator, pathType)

Expands specific node in the tree.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| path | string |	Path of the node |
| separator | string |	Separator character.<br>Optional, Default: ;. |
| pathType | string |	Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |




**Returns:**

boolean: 'true' if success, 'false' otherwise.



<a name="see.also.mscomctltreeview20.doexpand"></a>

<a name="DoSetCheck"></a>    
#### DoSetCheck(bcheck, path, separator, pathType)

Set 'checked' state of the specified node


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| bcheck | boolean |	Check state to set |
| path | string |	Path of the node |
| separator | string |	Separator character.<br>Optional, Default: ;. |
| pathType | string |	Path type. Can be one of 'name', 'id' or 'index'.<br>Optional, Default: name. |




**Returns:**

boolean: 'true' if success, 'false' otherwise.



<a name="see.also.mscomctltreeview20.dosetcheck"></a>

	
