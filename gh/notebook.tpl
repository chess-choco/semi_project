{%- extends 'basic.tpl' -%}

{%- block header -%}
<!DOCTYPE html>
<html>
<head>
{%- block html_head -%}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no,target-densitydpi=medium-dpi,viewport-fit=cover">
<meta name="format-detection" content="telephone=no,address=no,email=no"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
{% set nb_title = nb.metadata.get('title', '') or resources['metadata']['name'] %}
<title>{{nb_title}}</title>

{% for css in resources.inlining.css -%}
    <style type="text/css">
    {{ css }}
    </style>
{% endfor %}

<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}
div#notebook {
  overflow: visible;
  border-top: none;
}
@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  }
  div.output_wrapper {
    display: block;
    page-break-inside: avoid;
  }
  div.output {
    display: block;
    page-break-inside: avoid;
  }
}
</style>

<style type="text/css">
/* reset */
body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, pre, code, form, fieldset, legend, textarea, p, blockquote, th, td, input, select, textarea, button {
  margin: 0;
  padding: 0;
  font-family: Apple SD Gothic Neo,'Apple SD 산돌고딕 Neo',NanumGothic,'나눔고딕',ng,sans-serif;;
  -webkit-font-smoothing: antialiased;

  -webkit-font-smoothing: antialiased;
  -moz-font-smoothing: unset;
  -moz-osx-font-smoothing: grayscale;
  font-smoothing: antialiased;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  backface-visibility: hidden;

  text-rendering: auto;
  text-rendering: optimizeSpeed;
  text-rendering: optimizeLegibility;
  text-rendering: geometricPrecision;
  text-rendering: inherit;
}

fieldset, img {
  border: 0 none
}

dl, ul, ol, menu, li {
  list-style: none
}

blockquote, q {
  quotes: none
}

blockquote:before, blockquote:after, q:before, q:after {
  content: '';
  content: none
}

input, select, textarea, button {
  vertical-align: middle
}

input::-ms-clear {
  display: none
}

button {
  border: 0 none;
  background-color: transparent;
  cursor: pointer;
  outline: none;
  border-radius: 0px;
}

body {
  background: #fff;
  color: #333;
}

body,th,td,input,select,textarea,button {
  font-size:14px;
  line-height:1.5;
}

/* color값은 디자인가이드에 맞게사용 */
a {
  color: #333;
  text-decoration: none
}

a:active, a:hover {
  text-decoration: none
}

a:active {
  background-color: transparent
}

address, caption, cite, code, dfn, em, var {
  font-style: normal;
  font-weight: normal
}

/*
    Name:       Github Flavored
    Author:     aahoo

    Based on previous works of:
    CodeMirror template adapted for IPython Notebook by Nikhil Sonnad (https://github.com/nsonnad/base16-ipython-notebook)
    CodeMirror template by Jan T. Sott (https://github.com/idleberg/base16-chrome-devtools)
    Original Base16 color scheme by Chris Kempson (https://github.com/chriskempson/base16)
*/


/* UNCOMMENT THIS TO HIDE THE HEADER */

div#header-container {
  display: none !important;
}

/* UNCOMMENT THIS TO HIDE THE TOOLBAR
div#maintoolbar {
  display: none !important;
}
*/


/* GLOBALS */

* {
  line-height: 1.5;
  color: #333;
}
a {
  color: #4078c0;
}
.rendered_html a:link,
a:link {
  text-decoration: none;
}
body,
.CodeMirror {
  font-family: Roboto, "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;
}
body.notebook_app {
  background-color: white;
}
.container {
  max-width: 1000px;
}
div.code_cell .CodeMirror,
.cm-s-default .cm-comment,
.prompt,
code,
kbd,
pre,
samp {
  font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
}

/* INTRO PAGE */

div.list_container {
  border-radius: 0;
}
div.list_container > div {
  border-bottom: none;
}

/* NOTEBOOK */

div.navbar-default {
  border: none;
  background-color: transparent;
}
body > #header {
  background-color: #f7f7f7;
}
body > #header .header-bar {
  display: none;
}
div#notebook {
  border-top: none;
  padding: 20px 0 60px 0;
}
#menubar {
  margin-top: 0;
}
div#notebook-container {
  padding: 0;
  box-shadow: none;
}
.notebook_app > #header {
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.5);
}

/* input cell */

div.input {
  flex-direction: column;
}
div.input_prompt {
  color: #a71d5d;
  border: none;
}
div.input_area {
  border-radius: 0;
  border: none;
  background-color: #f7f7f7;
  box-shadow: 0 0, inset 0 0 0 1px #eee;
}

/* output cell */

div.output_area {
  flex-direction: column;
  padding: 10px;
  border-bottom: 1px dashed #ddd;
}
div.output_subarea {
  padding: 5px;
  padding-left: 10px;
}
div.output_prompt {
  color: #666;
}
div.output_text {
  line-height: inherit;
}
div.output_stderr {
  background-color: transparent;
}
div.output_scroll {
  box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.8);
}
div.output_collapsed {
  margin-top: 5px;
  padding: 10px;
  background: center url('data:image/svg+xml;utf8,<svg fill="#bbb" height="48" viewBox="0 0 24 24" width="48" xmlns="http://www.w3.org/2000/svg"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"/><path d="M0 0h24v24H0z" fill="none"/></svg>') no-repeat;
  text-indent: -9999px;
  border-radius: 0;
  border: none;
}
div.output_collapsed:hover,
div.output_collapsed:active {
  background: center url('data:image/svg+xml;utf8,<svg fill="#999" height="48" viewBox="0 0 24 24" width="48" xmlns="http://www.w3.org/2000/svg"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"/><path d="M0 0h24v24H0z" fill="none"/></svg>') no-repeat;
  background-color: rgba(0, 0, 0, .1);
  box-shadow: inset 0 0 0 1px #ccc;
}
div.out_prompt_overlay {
  height: auto;
  width: 18px;
  left: -10px;
  top: 5px;
  bottom: 5px;
  padding: 0!important;
  box-shadow: none !important;
}
div.out_prompt_overlay:hover {
  background-color: rgba(0, 0, 0, .1);
  box-shadow: inset 0 0 0 1px #ccc!important;
}
div.out_prompt_overlay:active {
  background-color: rgba(0, 0, 0, .2);
}

/* rendered html cell (mostly) */

.rendered_html h1,
.rendered_html h2,
.rendered_html h3,
.rendered_html h4,
.rendered_html h5,
.rendered_html h6,
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-family: inherit;
  line-height: inherit;
  font-weight: 300;
}
.rendered_html h1:first-child,
.rendered_html h1,
.rendered_html h2,
.rendered_html h3,
.rendered_html h4,
.rendered_html h5,
.rendered_html h6 {
  margin-top: .5em;
}
.rendered_html h1,
.cm-header-1 {
  font-size: 300%;
}
.rendered_html h2,
.cm-header-2 {
  font-size: 200%;
}
.rendered_html h3,
.cm-header-3 {
  font-size: 150%;
}
.rendered_html h4,
.cm-header-4 {
  font-size: 125%;
}
.rendered_html h5,
.cm-header-5 {
  font-size: 110%;
}
.rendered_html h6,
.cm-header-6 {
  font-size: 100%;
}
.rendered_html table,
.rendered_html th,
.rendered_html tr,
.rendered_html td {
  border: 1px #333 solid;
}
table.dataframe tr {
  border: 1px #ddd;
}

/* mixed cells */

div.cell {
  width: auto;
  /*margin-bottom: 5px;*/
}
div.cell.text_cell + div.cell.text_cell {
  /* to reduce the margin between two text cells */
  margin-top: -10px;
}
div.cell,
.edit_mode div.cell,
div.cell.selected,
.edit_mode div.cell.selected,
div.cell.jupyter-soft-selected,
div.cell.selected.jupyter-soft-selected {
  border: none;
  border-radius: 0;
  background: none;
  overflow-x: auto;
}
div.cell.selected,
div.cell.jupyter-soft-selected,
div.cell.selected.jupyter-soft-selected {
  box-shadow: 0 0 5px #333;
  background: #fff;
}
.edit_mode div.cell.selected {
  box-shadow: 0 0 5px #a71d5d;
}
div.rendered_html,
div.CodeMirror-lines {
  padding: 3px;
}
.edit_mode div.cell.selected .input_area {
  background: none;
}
div.code_cell .CodeMirror {
  font-size: 14px;
}
div.code_cell,
div.output_text {
  font-size: 14px;
  padding: 0;
}
div.output_area pre {
  color: #333;
}
div.prompt {
  min-width: auto;
  padding: 5px 5px 5px 0;
  line-height: inherit;
  text-align: left;
  border-radius: 0;
}
div.text_cell > div.prompt {
  display: none;
}
div.timing_area {
  border-top: dashed 1px #e8e8e8;
  text-align: right;
}

/* cell toolbar */

.celltoolbar {
  border: none;
  background: transparent;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: none;
}

/* style python code syntax */

div.CodeMirror span.CodeMirror-matchingbracket {
  color: #333 !important;
  box-shadow: inset 0px 0px 1px #ed6a43;
  border-radius: 2px;
}
.cm-s-ipython .CodeMirror-gutters {
  background-color: transparent;
  border-right: solid 1px #ddd;
  color: rgba(0, 0, 0, 0.3);
}
.cm-s-ipython .CodeMirror-linenumber {
  color: rgba(0, 0, 0, 0.3);
}
.cm-s-ipython span.cm-number {
  color: #0086b3;
}
.cm-s-ipython span.cm-property,
.cm-s-ipython span.cm-attribute {
  color: #689c00;
}
.cm-s-ipython span.cm-keyword {
  color: #a71d5d;
}
.cm-s-ipython span.cm-string {
  color: #183691;
}
.cm-s-ipython span.cm-operator {
  color: #a71d5d;
}
.cm-s-ipython span.cm-builtin {
  color: #0086b3;
}
.cm-s-ipython span.cm-variable {
  color: #333;
}
.cm-s-ipython span.cm-variable-2 {
  color: #ed6a43;
}
.cm-s-ipython span.cm-def {
  color: #795da3;
}
.cm-s-ipython span.cm-error {
  background: #e00;
  color: #fff!important;
}
.cm-s-ipython span.cm-bracket {
  color: #49483e;
}
.cm-s-ipython span.cm-comment {
  color: #999;
}
.cm-s-ipython span.cm-tag {
  color: #183691;
}
.cm-s-ipython span.cm-atom {
  color: #183691;
}

/* markdown style */

.cm-s-default .cm-tag {
  color: #183691;
}
.cm-s-default .cm-comment {
  color: #0086b3;
}
.cm-s-default .cm-string {
  color: #4078c0;
}
.cm-s-default .cm-link {
  color: #183691;
}
.cm-s-default .cm-header {
  color: #1d3e81;
}
.cm-s-default .cm-quote {
  color: #183691;
}

/* error in output */

span.ansiblack {
  color: #333;
}
span.ansiblue {
  color: #183691;
}
span.ansigray {
  color: #807d7c;
}
span.ansigreen {
  color: #3f8600;
}
span.ansipurple {
  color: #a71d5d;
}
span.ansired {
  color: #ed6a43;
}
span.ansiyellow {
  color: #e0b700;
}
span.ansicyan {
  color: #0086b3;
}
</style>

{%- endblock html_head -%}
</head>
{%- endblock header -%}

{% block body %}
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">
{{ super() }}
    </div>
  </div>
</body>
{%- endblock body %}

{# 코드 아웃풋의 공백 제거 #}
{% block codecell -%}
  {{ super() }}
{%- endblock codecell %}

{% block footer %}
{{ super() }}
</html>
{% endblock footer %}