#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const md2pug = new (require('markdown-to-pug'))();
const pug = require('pug');

// setup
const CURR_DIR = path.dirname(__filename);

const DOC_HOME = CURR_DIR;
const DOC_CONTENT_DIR = path.join(DOC_HOME,'content');
const DOC_TEMPLATE_DIR = path.join(DOC_HOME,'template');

const PROJ_HOME = path.join(CURR_DIR,'..');
const GITHUB_DOCS_DIR = path.join(PROJ_HOME,'docs');

const ROOT_HTML = fs.readFileSync(path.join(DOC_TEMPLATE_DIR,'root_template.html'),{encoding: 'utf-8'});

// var index_content = fs.readFileSync(path.join(DOC_CONTENT_DIR,'index.md'), {encoding: 'utf-8'});
var index_content = fs.readFileSync(path.join(PROJ_HOME,'README.md'), {encoding: 'utf-8'});

// start
var md = `# test`;
var content_pug = md2pug.render(index_content);

// handle img
content_pug = content_pug.replace(/(.*?)img\((.+?)\) (.+)/g,'$1img($2)')
content_pug = content_pug.replace(/h1 /g,'h1.title ');
content_pug = content_pug.replace(/h2 /g,'h2.title ');
content_pug = content_pug.replace(/h3 /g,'h3.title ');
content_pug = content_pug.replace(/h4 /g,'h4.title ');
content_pug = content_pug.replace(/table/g,'table.table.is-bordered.is-striped.is-narrow.is-hoverable.is-fullwidth');

// console.log(content_pug);
// process.exit();

html_result = pug.compile(content_pug)

html_result = ROOT_HTML.replace('{CONTENT_PLACEHOLDER}',html_result())
fs.writeFileSync(`${GITHUB_DOCS_DIR}/index.html`, html_result , {encoding:'utf-8'});