const path = require('path');
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
  entry: [
    './static/js/app.js'
  ],  // path to our input file
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './static'),  // path to our Django static directory
  },
  plugins: [
    new CopyPlugin({
      patterns: [
        {
          from: path.resolve(__dirname, './node_modules/bootstrap-icons/font/fonts'),
          to: path.resolve(__dirname, './static/fonts')
        },
        {
          from: path.resolve(__dirname, "node_modules", "@tabler/core/dist/css/tabler.min.css"),
          to: path.resolve(__dirname, './static/styles')
        },
        {
          from: path.resolve(__dirname, "node_modules", "@tabler/core/dist/js/tabler.min.js"),
          to: path.resolve(__dirname, './static/js')
        }
      ],
    }),
  ],
};