# HTML5
**HTML (Hypertext Markup Language)** is a standard markup language for creating and structuring web pages.<br>
Changes in HTML5:<br>
- **Semantic Elements:** Introduces semantic tags like **\<article\>, \<section\>, \<nav\>, etc.,** enhancing document structure.
- **Multimedia Support:** Native support for audio and video elements (**\<audio\>, \<video\>**).
- **Canvas and SVG:** Introduction of **\<canvas\>** for dynamic graphics and improved support for Scalable Vector Graphics (**\<svg\>**).
- **Local Storage:** Added local storage options (localStorage and sessionStorage) for web applications.
- **New Form Elements:** Enhanced form controls like **\<input\>** types (date, email, number) and <progress> and <meter> elements.
- **APIs and Web Workers:** Introduced various JavaScript APIs (e.g., Geolocation, Web Storage) and Web Workers for parallel processing.
- **Offline Web Applications:** Support for creating offline web applications using the Application Cache (AppCache) and Service Workers.
- **Improved Accessibility:** Emphasis on accessibility with features like **\<figure\>, \<figcaption\>, and \<summary\>.**
- **Cross-document Messaging:** Enhanced support for communication between documents using the postMessage API.
- **Responsive Web Design:** Better support for responsive web design with media queries.
- **Removal of Deprecated Elements:** Some older and less-used elements were deprecated or removed.
- **Global data- Attributes:** Introduction of custom data- attributes for embedding custom data private to the page or application.

## Various Tags of Html

- **\<html\>**: Defines the root element of an HTML document.
- **\<head\>**: Contains metadata about the HTML document, such as title, links, and scripts.
- **\<title\>**: Sets the title of the HTML document, displayed in the browser's title bar or tab.
- **\<body\>**: Contains the content of the HTML document, such as text, images, links, etc.
- **\<h1\>** to **\<h6\>**: Define headings of different levels, with **\<h1\>** being the highest and **\<h6\>** the lowest.
- **\<p\>**: Represents a paragraph of text.
- **\<a\>**: Creates hyperlinks to link to other documents or resources.
- **\<img\>**: Embeds images in the document.
- **\<ul\>**: Defines an unordered list.
- **\<ol\>**: Defines an ordered list.
- **\<li\>**: Represents a list item within **\<ul\>** or **\<ol\>**.
- **\<div\>**: A generic container used for layout and grouping other HTML elements.
- **\<span\>**: A generic container used for applying styles or scripting to a specific part of text.
- **\<br\>**: Represents a line break.
- **\<hr\>**: Represents a thematic break or horizontal line.
- **\<em\>**: Emphasizes text, usually displayed in italics.
- **\<strong\>**: Represents strong importance or seriousness, usually displayed in bold.
- **\<u\>**: Underlines text.
- **\<i\>**: Represents text in an alternate voice or mood, usually displayed in italics.
- **\<b\>**: Represents bold text.
- **\<blockquote\>**: Represents a block of text quoted from another source.
- **\<code\>**: Represents a single line of code.
- **\<pre\>**: Represents preformatted text, preserving both spaces and line breaks.
- **\<table\>**: Defines a table.
- **\<tr\>**: Represents a table row.
- **\<th\>**: Represents a table header cell.
- **\<td\>**: Represents a table data cell.
- **\<form\>**: Represents an HTML form for user input.
- **\<input\>**: Represents an input field within a form.
- **\<button\>**: Represents a clickable button.

# CSS
CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation and formatting of HTML or XML documents, defining how elements are displayed on web pages.

## Box Model
- **Components**: *content, padding, border, margin*
- **Example**:
```css
.box {
    width: 100px;
    padding: 10px;
    border: 1px solid #000;
    margin: 20px;
}
```

## Inline versus Block Elements. Examples.
- **Inline**: Share the same line.
- **Block**: Occupy full width, start on a new line.
- **Example**:
```css
.inline {
    display: inline;
}

.block {
    display: block;
}

```

## Positioning: Relative/Absolute
- **relative**: Relative to its normal position.
- **absolute**: Positioned relative to the nearest positioned ancestor.
- **Example**:
```css
.relative {
    position: relative;
}

.absolute {
    position: absolute;
}

```

## Common CSS structural classes
- *.container, .row, .col*
- **Example**:
```css
  <div class="container">
    <div class="row">
        <div class="col">Content</div>
    </div>
  </div>
```

## Common CSS syling classes
- *.text-center, .bg-primary, .rounded*
- **Example**:
```css
<div class="text-center bg-primary rounded">Styled Content</div>
```

## CSS Specificity
- Specificity hierarchy: Inline > ID > Class > Element
- **Example**:
```css
#specific {
    color: red;
}

.specific {
    color: blue;
}
```

## CSS Responsive Queries
- Media queries for responsiveness.
- **Example**:
```css
@media screen and (max-width: 600px) {
    /* Styles for small screens */
}

```

## Common header meta tags
- **Example**:
```css
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Other meta tags -->
</head>
```

## Flexboxfroggy

### justify-content - *horizontally*

- **flex-start:** Items align to the left side of the container.
- **flex-end:** Items align to the right side of the container.
- **center:** Items align at the center of the container.
- **space-between:** Items display with equal spacing between them.
- **space-around:** Items display with equal spacing around them.

**Example**

```css
#pond {
    display: flex;
    justify-content: flex-end;
}
```

### Align-items && Align-self - *vertically*

- **flex-start:** Items align to the top of the container.
- **flex-end:** Items align to the bottom of the container.
- **center:** Items align at the vertical center of the container.
- **baseline:** Items display at the baseline of the container.
- **stretch:** Items are stretched to fit the container.

**Example**

```css
#pond {
  display: flex;
  align-items: flex-start;
}

.yellow {
  align-self: flex-end;
}
```

### Align-content
**Align-content vs Align-items ?**
*Align-content* is used for controlling the alignment of flex lines in multi-line flex containers, <br>
*Align-items* is used for aligning individual flex items within both single-line and multi-line flex containers.
- **flex-start**
- **flex-end**
- **center**
- **space-between**
- **space-around**
- **space-evenly**
- **stretch (default)**

### Flex-direction - *Alter Direction*

- **row:** Items are placed the same as the text direction.
- **row-reverse:** Items are placed opposite to the text direction.
- **column:** Items are placed top to bottom.
- **column-reverse:** Items are placed bottom to top.

**Example**

```css
#pond {
    display: flex;
    flex-direction: row-reverse
}
```

### Order 
The order property specifies the order of a flexible item relative to the rest of the flexible items inside the same container.

**Example**

```css
.red {
  order: -3;
}
```

### Flex-wrap

- **nowrap:** Every item is fit to a single line.
- **wrap:** Items wrap around to additional lines.
- **wrap-reverse**

**Example**

```css
#pond {
  display: flex;
  flex-wrap: wrap;
}
```

### Flex-flow
A Happy Marriage of flex-direction and flex-wrap.

**Example**

```css
#pond {
  display: flex;
  flex-flow: column wrap;
}
```



## Grid Garden

### Grid-template-rows & columns
*Used to Initialize Grid*
We can divide the rows & columns with percentage, fractions etc mentioning each of that part seperated by spaces, so that it sums up to the total value. We can use **repeat** for lazy coding as below.

```css
#garden {
	display: grid;
	grid-template-columns: repeat(8,12.5%);
	grid-template-rows: 20% 20% 20% 20% 20%;
}
```

**grid-template-columns** doesn't just accept values in **percentages**, but also length units like **pixels** and **ems**. You can even mix different units together.<br> **fr == fraction** here the region is divided into **1/6 and 5/6**

```css
#garden {
	display: grid;
	grid-template-columns: 100px 3em 40%;
	grid-template-rows: 1fr 5fr;
}
```

**grid-template** is a shorthand property that combines *grid-template-rows and grid-template-columns*.

For example, **grid-template: 50% 50% / 200px;** will create a grid with two rows that are 50% each, and one column that is 200 pixels wide.

```css
#garden {
  display: grid;
  grid-template:  50% 50% / 200px;
}

```

### Grid : column/row | start/end

**grid-column-start** starts from the index mentioned, **grid-column-end** ends at the index mentioned.
- *start* doesn't start from 0th index but 1 which is the grid line. This 1 is same as -2.
- *end* at intended-index + 1
- start and end index can be interchanged. i.e *start_index > end_index* possible.
- negative value in index states that it starts from the opposite end of the number line.

```css
#water {
  grid-column-start: 3;
  grid-column-end: 6;
}
```
**Grid-column & Grid-row -** Combines start and end like start/end.

```css
#water {
  grid-column: 3/6;
  grid-row: 3/5;
}
```

### span
- spans an area instead of a discrete end point
- Only works with positive values

*Below code spans 3 blocks while ending at 6.*

```css
#water {
  grid-column-start: span 3;
  grid-column-end: 6;
}
```

### Grid with span
*Below code spans 3 blocks while ending at 5.* <br>
**span-region / ends_at**

```css
#water {
  grid-column: span 3/5;
  grid-row: span 3/5;
}
```

### Grid-area
Accepts four values separated by slashes
**grid-area: grid-row-start, grid-column-start, grid-row-end, grid-column-end**
```css
#water {
  grid-area: 1/2/4/6;
}
```

### Order
To change the order of placement of a particular class or id.
By default, all grid items have an order of 0, but this can be set to any positive or negative value, similar to z-index.
