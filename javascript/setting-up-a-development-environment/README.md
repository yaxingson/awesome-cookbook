# Table of Contents

## Choosing a Code Editor

## Using the Developer Console in Your Browser

## Running Blocks of Code in the Developer Console

## Using Strict Mode to Catch Common Mistakes

```js
'use strict';

```

## Filling in HTML Boilerplate with Emmet Shortcuts

## Installing the npm Package Manager (with Node.js)

```sh
$ node -v
$ npm -v


```

## Downloading a Package with npm

```sh
$ npm list -g --depth 0

```

## Updating a Package with npm

```sh
$ npm update

$ npm outdated

```

[npm-check-updates](https://github.com/raineorshine/npm-check-updates)


## Setting Up a Local Test Server

```sh
$ npm install lite-server --save-dev

$ npx lite-server

```


## Enforcing Code Standards with a Linter

```sh
$ npm install eslint --save-dev

$ npx eslint --init


```


## Styling Code Consistently with a Formatter

```sh
$ npm install --save-dev eslint-config-prettier

```

.eslintrc.json:

```json
{
  "env": {
    "browser": true,
    "es2021": true
   },
  "extends": ["eslint:recommended", "prettier"],
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "rule": {}
}

```


## Experimenting in a JavaScript Playground

JavaScript Playgrounds:

- [jsfiddle](https://jsfiddle.net/)
- [jsbin](https://jsbin.com/)
- [codepen](https://codepen.io/)
- [codesandbox](https://codesandbox.io/)
- [glitch](https://glitch.com/)
