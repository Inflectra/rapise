# Win32Text

This is generic Win32 edit box. Use DoSetText to set the value of the edit box and GetText to read current value.
 
Extends <link displaytype="text" defaultstyle="true" type="topiclink" href="SeSSimulatedObject" styleclass="Normal" translate="true">SeSSimulatedObject</link>.





**Behavior Pattern: Win32TextEditable**


<!-- ============================== property summary ========================== -->

	

### Property Summary

| **Property** | **Description** | **Getter** | **Setter** |
| ------------ | --------------- | ---------- | ---------- |
| [Text](#Text) | Text of the object, 'false' if text can not be read. | GetText | SetText |



	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[DoSetText](#DoSetText) | Sets text value of this object. |




<!-- ============================== property detail ========================== -->
	
### Property Detail
		
<a name="Text"></a>
#### Text


Text of the object, 'false' if text can not be read.

			
	
			
Type: string
			
			
Accessors: GetText, SetText
			
		
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="DoSetText"></a>    
#### DoSetText(val)

Sets text value of this object.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| val | string |	Text value. |




**Returns:**

boolean: 'true' if success, 'false' otherwise.



<a name="see.also.win32text.dosettext"></a>

	
