Summary: Global object. Use it to perform actions not related to a particular object. You do not need to

# Android

Global object. Use it to perform actions not related to a particular object. You do not need torecord or learn this object, it is always automatically available in any test.






<!-- ============================== property summary ========================== -->

	
<!-- ============================== action summary ========================== -->



### Action Summary

|  **Action** | **Description** | 
| ----------- | --------------- |
|	[DoFlick](#doflick) | Flick action. |
|	[DoGoToUrl](#dogotourl) | Opens URL in active browser. |
|	[DoPressBack](#dopressback) | Presses Back button. |
|	[DoPressHome](#dopresshome) | Presses Home button. |
|	[DoPressKeyCode](#dopresskeycode) | Presses key with code. |
|	[DoPressMenu](#dopressmenu) | Presses Menu button. |
|	[DoScreenshot](#doscreenshot) | Makes screenshot of a device. |
|	[DoStartActivity](#dostartactivity) | Starts activity. |
|	[DoStartVideoRecording](#dostartvideorecording) | Starts video recording on a device. |
|	[DoStopVideoRecording](#dostopvideorecording) | Stops video recording on a device. |
|	[DoSwipe](#doswipe) | Swipe action. |
|	[DoTap](#dotap) | Tap screen. |
|	[GetCapability](#getcapability) | Gets capability with specified name. |
|	[GetContext](#getcontext) | Gets current context. |
|	[SetContext](#setcontext) | Sets context. |




<!-- ============================== property detail ========================== -->
	
	
<!-- ============================== action detail ========================== -->
	
### Action Detail
		
<a name="DoFlick"></a>    
#### DoFlick

Flick action.

```javascript
DoFlick(endX, endY, startX, startY, touchCount) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| endX | number |	x coordinate where swipe ends (in pixels or relative units) |
| endY | number |	y coordinate where swipe ends (in pixels or relative units) |
| startX | number |	x coordinate where swipe begins (in pixels or relative units)<br>Optional. |
| startY | number |	y coordinate where swipe begins (in pixels or relative units)<br>Optional. |
| touchCount | number |	how many fingers to swipe with<br>Optional. |




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.doflick"></a>

<a name="DoGoToUrl"></a>    
#### DoGoToUrl

Opens URL in active browser.

```javascript
DoGoToUrl(url) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| url | string |	 |




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dogotourl"></a>

<a name="DoPressBack"></a>    
#### DoPressBack

Presses Back button.

```javascript
DoPressBack() 
```




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dopressback"></a>

<a name="DoPressHome"></a>    
#### DoPressHome

Presses Home button.

```javascript
DoPressHome() 
```




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dopresshome"></a>

<a name="DoPressKeyCode"></a>    
#### DoPressKeyCode

Presses key with code.

```javascript
DoPressKeyCode(keyCode) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| keyCode | number |	Key code: http://developer.android.com/reference/android/view/KeyEvent.html |




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dopresskeycode"></a>

<a name="DoPressMenu"></a>    
#### DoPressMenu

Presses Menu button.

```javascript
DoPressMenu() 
```




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dopressmenu"></a>

<a name="DoScreenshot"></a>    
#### DoScreenshot

Makes screenshot of a device.

```javascript
DoScreenshot() 
```




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.doscreenshot"></a>

<a name="DoStartActivity"></a>    
#### DoStartActivity

Starts activity.

```javascript
DoStartActivity(appPackage, appActivity) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| appPackage | string |	Package name. |
| appActivity | string |	Activity name. |




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dostartactivity"></a>

<a name="DoStartVideoRecording"></a>    
#### DoStartVideoRecording

Starts video recording on a device.

```javascript
DoStartVideoRecording() 
```




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dostartvideorecording"></a>

<a name="DoStopVideoRecording"></a>    
#### DoStopVideoRecording

Stops video recording on a device.

```javascript
DoStopVideoRecording() 
```




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dostopvideorecording"></a>

<a name="DoSwipe"></a>    
#### DoSwipe

Swipe action.

```javascript
DoSwipe(endX, endY, startX, startY, duration, touchCount) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| endX | number |	x coordinate where swipe ends (in pixels or relative units) |
| endY | number |	y coordinate where swipe ends (in pixels or relative units) |
| startX | number |	x coordinate where swipe begins (in pixels or relative units)<br>Optional. |
| startY | number |	y coordinate where swipe begins (in pixels or relative units)<br>Optional. |
| duration | number |	time (in seconds) to spend performing the swipe/drag<br>Optional. |
| touchCount | number |	how many fingers to swipe with<br>Optional. |




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.doswipe"></a>

<a name="DoTap"></a>    
#### DoTap

Tap screen.

```javascript
DoTap(x, y, duration, tapCount, touchCount) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| x | number |	x coordinate to tap (in pixels or relative units)<br>Optional. |
| y | number |	y coordinate to tap (in pixels or relative units)<br>Optional. |
| duration | number |	how long (in seconds) to tap<br>Optional. |
| tapCount | number |	how many times to tap<br>Optional. |
| touchCount | number |	how many fingers to tap with<br>Optional. |




**Returns:**

'true' if successful, 'false' otherwise.



<a name="see.also.android.dotap"></a>

<a name="GetCapability"></a>    
#### GetCapability

Gets capability with specified name.

```javascript
GetCapability(name) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| name | string |	Name of a capability. |




**Returns:**

Capability string.



<a name="see.also.android.getcapability"></a>

<a name="GetContext"></a>    
#### GetContext

Gets current context.

```javascript
GetContext() 
```




**Returns:**

Either NATIVE_APP or WEBVIEW_1.



<a name="see.also.android.getcontext"></a>

<a name="SetContext"></a>    
#### SetContext

Sets context.

```javascript
SetContext(name) 
```


**Parameters:**

|	**Name** | **Type** | **Description** |
| ---------- | -------- | --------------- |
| name | string |	Either NATIVE_APP or WEBVIEW_1. |





<a name="see.also.android.setcontext"></a>

	

