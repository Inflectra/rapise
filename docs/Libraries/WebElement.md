Summary: This is a JavaScript wrapper for RemoteWebElement of Selenium .NET library.

# WebElement

This is a JavaScript wrapper for RemoteWebElement of Selenium .NET library.For code complete feature use class name WebElementWrapper, e.g. <br><br><p style="margin-left: 30px;"><code>var /&#42;&#42;WebElementWrapper&#42;/el = WebDriver.FindElementById('username');</code></p>






<!-- ============================== property summary ========================== -->

	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[Clear](#clear) | Clears the content of this element. |
|	[Click](#click) | Clicks this element. |
|	[ClickAt](#clickat) | Clicks this element at the specified location. |
|	[ContextClick](#contextclick) | Opens context menu for this element. |
|	[DoubleClick](#doubleclick) | Performs double click on this element. |
|	[FindElementByClassName](#findelementbyclassname) | Finds the first element in the page that matches the CSS Class supplied. |
|	[FindElementByCssSelector](#findelementbycssselector) | Finds the first element matching the specified CSS selector. |
|	[FindElementById](#findelementbyid) | Finds the first element in the page that matches the ID supplied. |
|	[FindElementByLinkText](#findelementbylinktext) | Finds the first of elements that match the link text supplied. |
|	[FindElementByName](#findelementbyname) | Finds the first of elements that match the name supplied. |
|	[FindElementByPartialLinkText](#findelementbypartiallinktext) | Finds the first of elements that match the part of the link text supplied. |
|	[FindElementByTagName](#findelementbytagname) | Finds the first of elements that match the DOM Tag supplied. |
|	[FindElementByXPath](#findelementbyxpath) | Finds the first of elements that match the XPath supplied. |
|	[FindElementsByClassName](#findelementsbyclassname) | Finds a list of elements that match the class name supplied. |
|	[FindElementsByCssSelector](#findelementsbycssselector) | Finds all elements matching the specified CSS selector. |
|	[FindElementsById](#findelementsbyid) | Finds the first element in the page that matches the ID supplied. |
|	[FindElementsByLinkText](#findelementsbylinktext) | Finds a list of elements that match the link text supplied. |
|	[FindElementsByName](#findelementsbyname) | Finds a list of elements that match the name supplied. |
|	[FindElementsByPartialLinkText](#findelementsbypartiallinktext) | Finds a list of elements that match the part of the link text supplied. |
|	[FindElementsByTagName](#findelementsbytagname) | Finds a list of elements that match the DOM Tag supplied. |
|	[FindElementsByXPath](#findelementsbyxpath) | Finds a list of elements that match the XPath supplied. |
|	[GetAttribute](#getattribute) | Gets the value of the specified attribute for this element. |
|	[GetCoordinates](#getcoordinates) | Gets a 'Point' object containing the coordinates of theupper-left corner of this element relative to the upper-leftcorner of the page. |
|	[GetCssValue](#getcssvalue) | Gets the value of a CSS property of this element. |
|	[GetDisplayed](#getdisplayed) | Gets a value indicating whether or not this element is displayed. |
|	[GetEnabled](#getenabled) | Gets a value indicating whether or not this element is enabled. |
|	[GetHashCode](#gethashcode) | Method to get the hash code of the element. |
|	[GetLocation](#getlocation) | Gets a 'Point' object containing the coordinates of theupper-left corner of this element relative to the upper-leftcorner of the page. |
|	[GetLocationOnScreenOnceScrolledIntoView](#getlocationonscreenoncescrolledintoview) | Gets the point where the element would be when scrolled into view. |
|	[GetSelected](#getselected) | Gets a value indicating whether or not this element is selected. |
|	[GetSize](#getsize) | Gets a 'Size' object containing the height and width of this element. |
|	[GetTagName](#gettagname) | Gets the tag name of this element. |
|	[GetText](#gettext) | Gets the innerText of this element, without any leading ortrailing whitespace, and with other whitespace collapsed. |
|	[SelectOptionByText](#selectoptionbytext) | Selects option from select element. |
|	[SendKeys](#sendkeys) | Simulates typing text into the element. |
|	[Submit](#submit) | Submits this element to the web server. |




<!-- ============================== property detail ========================== -->
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="Clear"></a>    
#### Clear

Clears the content of this element.

```javascript
Clear() 
```





<a name="see.also.webelement.clear"></a>

<a name="Click"></a>    
#### Click

Clicks this element.

```javascript
Click() 
```





<a name="see.also.webelement.click"></a>

<a name="ClickAt"></a>    
#### ClickAt

Clicks this element at the specified location.

```javascript
ClickAt(x, y) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| x | number |	 |
| y | number |	 |





<a name="see.also.webelement.clickat"></a>

<a name="ContextClick"></a>    
#### ContextClick

Opens context menu for this element.

```javascript
ContextClick() 
```





<a name="see.also.webelement.contextclick"></a>

<a name="DoubleClick"></a>    
#### DoubleClick

Performs double click on this element.

```javascript
DoubleClick() 
```





<a name="see.also.webelement.doubleclick"></a>

<a name="FindElementByClassName"></a>    
#### FindElementByClassName

Finds the first element in the page that matches the CSS Class supplied.

```javascript
FindElementByClassName(className) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| className | string |	CSS class name of the element. |




**Returns:**

element or null.



<a name="see.also.webelement.findelementbyclassname"></a>

<a name="FindElementByCssSelector"></a>    
#### FindElementByCssSelector

Finds the first element matching the specified CSS selector.

```javascript
FindElementByCssSelector(cssSelector) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| cssSelector | string |	The CSS selector to match. |




**Returns:**

element ot null.



<a name="see.also.webelement.findelementbycssselector"></a>

<a name="FindElementById"></a>    
#### FindElementById

Finds the first element in the page that matches the ID supplied.

```javascript
FindElementById(id) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| id | string |	ID of the element. |




**Returns:**

element or null.



<a name="see.also.webelement.findelementbyid"></a>

<a name="FindElementByLinkText"></a>    
#### FindElementByLinkText

Finds the first of elements that match the link text supplied.

```javascript
FindElementByLinkText(linkText) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| linkText | string |	Link text of element. |




**Returns:**

element or null.



<a name="see.also.webelement.findelementbylinktext"></a>

<a name="FindElementByName"></a>    
#### FindElementByName

Finds the first of elements that match the name supplied.

```javascript
FindElementByName(name) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| name | string |	Name of the element on the page. |




**Returns:**

element or null.



<a name="see.also.webelement.findelementbyname"></a>

<a name="FindElementByPartialLinkText"></a>    
#### FindElementByPartialLinkText

Finds the first of elements that match the part of the link text supplied.

```javascript
FindElementByPartialLinkText(partialLinkText) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| partialLinkText | string |	Part of the link text. |




**Returns:**

element or null.



<a name="see.also.webelement.findelementbypartiallinktext"></a>

<a name="FindElementByTagName"></a>    
#### FindElementByTagName

Finds the first of elements that match the DOM Tag supplied.

```javascript
FindElementByTagName(tagName) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| tagName | string |	DOM tag Name of the element being searched. |




**Returns:**

element or null.



<a name="see.also.webelement.findelementbytagname"></a>

<a name="FindElementByXPath"></a>    
#### FindElementByXPath

Finds the first of elements that match the XPath supplied.

```javascript
FindElementByXPath(xpath) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| xpath | string |	xpath to the element. |




**Returns:**

element or null.



<a name="see.also.webelement.findelementbyxpath"></a>

<a name="FindElementsByClassName"></a>    
#### FindElementsByClassName

Finds a list of elements that match the class name supplied.

```javascript
FindElementsByClassName(className) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| className | string |	className of the element. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbyclassname"></a>

<a name="FindElementsByCssSelector"></a>    
#### FindElementsByCssSelector

Finds all elements matching the specified CSS selector.

```javascript
FindElementsByCssSelector(cssSelector) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| cssSelector | string |	The CSS selector to match. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbycssselector"></a>

<a name="FindElementsById"></a>    
#### FindElementsById

Finds the first element in the page that matches the ID supplied.

```javascript
FindElementsById(id) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| id | string |	ID of the element. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbyid"></a>

<a name="FindElementsByLinkText"></a>    
#### FindElementsByLinkText

Finds a list of elements that match the link text supplied.

```javascript
FindElementsByLinkText(linkText) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| linkText | string |	Link text of element. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbylinktext"></a>

<a name="FindElementsByName"></a>    
#### FindElementsByName

Finds a list of elements that match the name supplied.

```javascript
FindElementsByName(name) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| name | string |	Name of the element on the page. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbyname"></a>

<a name="FindElementsByPartialLinkText"></a>    
#### FindElementsByPartialLinkText

Finds a list of elements that match the part of the link text supplied.

```javascript
FindElementsByPartialLinkText(partialLinkText) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| partialLinkText | string |	Part of the link text. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbypartiallinktext"></a>

<a name="FindElementsByTagName"></a>    
#### FindElementsByTagName

Finds a list of elements that match the DOM Tag supplied.

```javascript
FindElementsByTagName(tagName) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| tagName | string |	DOM tag Name of the element being searched. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbytagname"></a>

<a name="FindElementsByXPath"></a>    
#### FindElementsByXPath

Finds a list of elements that match the XPath supplied.

```javascript
FindElementsByXPath(xpath) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| xpath | string |	xpath to the element. |




**Returns:**

array of elements.



<a name="see.also.webelement.findelementsbyxpath"></a>

<a name="GetAttribute"></a>    
#### GetAttribute

Gets the value of the specified attribute for this element.

```javascript
GetAttribute(attributeName) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| attributeName |  |	 |





<a name="see.also.webelement.getattribute"></a>

<a name="GetCoordinates"></a>    
#### GetCoordinates

Gets a 'Point' object containing the coordinates of theupper-left corner of this element relative to the upper-leftcorner of the page.

```javascript
GetCoordinates() 
```





<a name="see.also.webelement.getcoordinates"></a>

<a name="GetCssValue"></a>    
#### GetCssValue

Gets the value of a CSS property of this element.

```javascript
GetCssValue(propertyName) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| propertyName |  |	 |





<a name="see.also.webelement.getcssvalue"></a>

<a name="GetDisplayed"></a>    
#### GetDisplayed

Gets a value indicating whether or not this element is displayed.

```javascript
GetDisplayed() 
```





<a name="see.also.webelement.getdisplayed"></a>

<a name="GetEnabled"></a>    
#### GetEnabled

Gets a value indicating whether or not this element is enabled.

```javascript
GetEnabled() 
```





<a name="see.also.webelement.getenabled"></a>

<a name="GetHashCode"></a>    
#### GetHashCode

Method to get the hash code of the element.

```javascript
GetHashCode() 
```





<a name="see.also.webelement.gethashcode"></a>

<a name="GetLocation"></a>    
#### GetLocation

Gets a 'Point' object containing the coordinates of theupper-left corner of this element relative to the upper-leftcorner of the page.

```javascript
GetLocation() 
```





<a name="see.also.webelement.getlocation"></a>

<a name="GetLocationOnScreenOnceScrolledIntoView"></a>    
#### GetLocationOnScreenOnceScrolledIntoView

Gets the point where the element would be when scrolled into view.

```javascript
GetLocationOnScreenOnceScrolledIntoView() 
```





<a name="see.also.webelement.getlocationonscreenoncescrolledintoview"></a>

<a name="GetSelected"></a>    
#### GetSelected

Gets a value indicating whether or not this element is selected.

```javascript
GetSelected() 
```





<a name="see.also.webelement.getselected"></a>

<a name="GetSize"></a>    
#### GetSize

Gets a 'Size' object containing the height and width of this element.

```javascript
GetSize() 
```





<a name="see.also.webelement.getsize"></a>

<a name="GetTagName"></a>    
#### GetTagName

Gets the tag name of this element.

```javascript
GetTagName() 
```





<a name="see.also.webelement.gettagname"></a>

<a name="GetText"></a>    
#### GetText

Gets the innerText of this element, without any leading ortrailing whitespace, and with other whitespace collapsed.

```javascript
GetText() 
```





<a name="see.also.webelement.gettext"></a>

<a name="SelectOptionByText"></a>    
#### SelectOptionByText

Selects option from select element.

```javascript
SelectOptionByText(option) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| option |  |	 |





<a name="see.also.webelement.selectoptionbytext"></a>

<a name="SendKeys"></a>    
#### SendKeys

Simulates typing text into the element.

```javascript
SendKeys(text) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| text |  |	 |





<a name="see.also.webelement.sendkeys"></a>

<a name="Submit"></a>    
#### Submit

Submits this element to the web server.

```javascript
Submit() 
```





<a name="see.also.webelement.submit"></a>

	

