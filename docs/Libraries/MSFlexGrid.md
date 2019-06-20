# MSFlexGrid

Extends [ActiveXObject](ActiveXObject.md)

Extends [SeSSimulatedObject](SeSSimulatedObject.md)





**Behavior Pattern: MSFlexGridBehavior**


<!-- ============================== property summary ========================== -->

	

### Property Summary

| **Property** | **Description** | **Getter** | **Setter** |
| ------------ | --------------- | ---------- | ---------- |
| [Cell](#Cell) | Text of the specified cell. | GetCell |  |
| [ColumnCount](#ColumnCount) | Number of columns in the table. | GetColumnCount |  |
| [ColumnName](#ColumnName) | Caption of a column. | GetColumnName |  |
| [RowCount](#RowCount) | Number of rows in the table. | GetRowCount |  |
| [SelectedColumn](#SelectedColumn) | Index of the selected column. | GetSelectedColumn |  |
| [SelectedRow](#SelectedRow) | Index of the selected row. | GetSelectedRow |  |
| [Text](#Text) | Text of the currently focused cell. | GetText |  |



	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[DoClickCell](#DoClickCell) | Clicks the specified cell. |
|	[DoClickText](#DoClickText) | Clicks on a specific text inside the grid. |
|	[DoFullText](#DoFullText) | Returns text representation of the table. |




<!-- ============================== property detail ========================== -->
	
### Property Detail
		
<a name="Cell"></a>
#### Cell


Text of the specified cell.

			
	
			
Type: string
			
			
Accessors: GetCell
			
		
<a name="ColumnCount"></a>
#### ColumnCount


Number of columns in the table.

			
	
			
Type: number
			
			
Accessors: GetColumnCount
			
		
<a name="ColumnName"></a>
#### ColumnName


Caption of a column.

			
**Getter Parameters:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |	
| col | number | Zero-based index of the column. |


	
			
Type: string
			
			
Accessors: GetColumnName
			
		
<a name="RowCount"></a>
#### RowCount


Number of rows in the table.

			
	
			
Type: number
			
			
Accessors: GetRowCount
			
		
<a name="SelectedColumn"></a>
#### SelectedColumn


Index of the selected column.

			
	
			
Type: number
			
			
Accessors: GetSelectedColumn
			
		
<a name="SelectedRow"></a>
#### SelectedRow


Index of the selected row.

			
	
			
Type: number
			
			
Accessors: GetSelectedRow
			
		
<a name="Text"></a>
#### Text


Text of the currently focused cell.

			
	
			
Type: string
			
			
Accessors: GetText
			
		
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="DoClickCell"></a>    
#### DoClickCell(row, col, clickType, xOffset, yOffset)

Clicks the specified cell.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| row | number \| string |	Zero-based index if the row or text of a cell in the specified column. |
| col | string \| number |	Zero-based index of the column or column name. |
| clickType | string |	Type of click, can be one of "L" - left click, "LD" - double left click, "R" - right click, "RD" - double right click, "M" - middle click, "MD" - double middle click, "N" - don't click<br>Optional, Default: L. |
| xOffset | number |	X offset to click within node. Default is a center.<br>Optional. |
| yOffset | number |	Y offset to click within node. Default is a center.<br>Optional. |




**Returns:**

boolean: 'true' if successful, 'false' otherwise



<a name="see.also.msflexgrid.doclickcell"></a>

<a name="DoClickText"></a>    
#### DoClickText(textOrRegexp, clickType)

Clicks on a specific text inside the grid.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| textOrRegexp | string |	Text (or regex: expression) to search in the grid. |
| clickType | string |	Type of click, can be one of "L" - left click, "LD" - double left click, "R" - right click, "RD" - double right click, "M" - middle click, "MD" - double middle click, "N" - don't click<br>Optional, Default: L. |




**Returns:**

'true' if successful, 'false' otherwise



<a name="see.also.msflexgrid.doclicktext"></a>

<a name="DoFullText"></a>    
#### DoFullText()

Returns text representation of the table.




**Returns:**

string | <br>boolean: Text representation of the grid, 'true' if the file was successfully written, 'false' otherwise.



<a name="see.also.msflexgrid.dofulltext"></a>

	
