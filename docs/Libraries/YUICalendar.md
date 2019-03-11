# YUICalendar

YUI Calendar.
 
Extends HTMLObject.

Extends SeSSimulatedObject.





**Behavior Pattern: YUICalendarBehavior**


<!-- ============================== property summary ========================== -->

	

### Property Summary

| **Property** | **Description** | **Getter** | **Setter** |
| ------------ | --------------- | ---------- | ---------- |
| [Month](#Month) | Current month displayed by the date picker. | GetMonth |  |



	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[DoNextMonth](#DoNextMonth) | Clicks on 'Next Month' selector. |
|	[DoPrevMonth](#DoPrevMonth) | Clicks on 'Previous Month' selector. |
|	[DoSelectDate](#DoSelectDate) | Selects specific date in the date picker. |




<!-- ============================== property detail ========================== -->
	
### Property Detail
		
<a name="Month"></a>
#### Month


Current month displayed by the date picker.

			
	
			
Type: string|number
			
			
Accessors: GetMonth
			
		
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="DoNextMonth"></a>    
#### DoNextMonth()

Clicks on 'Next Month' selector.




**Returns:**

boolean: 'true' if success, 'false' otherwise



<a name="see.also.yuicalendar.donextmonth"></a>

<a name="DoPrevMonth"></a>    
#### DoPrevMonth()

Clicks on 'Previous Month' selector.




**Returns:**

boolean: 'true' if success, 'false' otherwise



<a name="see.also.yuicalendar.doprevmonth"></a>

<a name="DoSelectDate"></a>    
#### DoSelectDate(dateValue)

Selects specific date in the date picker.


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| dateValue | number |	New date to select |




**Returns:**

boolean: 'true' if success, 'false' otherwise



<a name="see.also.yuicalendar.doselectdate"></a>

	
