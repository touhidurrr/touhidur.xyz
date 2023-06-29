const maxWidth = 100;
const minWidth = 40;
const minHeight = 12;
const maxHeight = 30;

const getHTML = (paste) => `<!DOCTYPE html>
<html>
  <head>
    <title>See your Paste!</title>
    <meta name="viewport" content="width=device-width">
  </head>
  <body align="center">
    <textarea id="text"
      rows="${Math.max(minHeight, Math.min(maxHeight, paste.split('\n').length))}"
      cols="${Math.max(maxWidth, Math.min(minWidth, Math.max(...paste.split('\n').map(l => l.length))))}"
    >${paste}</textarea>
    <br><br>
    <button onclick="copy()">Copy to Clipboard!</button>
    <script>
      const text = document.getElementById('text');
      function copy() {
        navigator.clipboard.writeText(text.value);
      }
      function setTextAreaSize() {
        const lines = text.value.split('\n');
        const lineLength = Math.max(...lines.map(line => line.length));
        text.rows = Math.max(${minHeight}, Math.min(${maxHeight}, lines.length));
        text.cols = Math.max(${maxWidth}, Math.min(${minWidth}, lineLength));
      }
      text.onchange = setTextAreaWidth;
    </script>
  </body>
</html>`;

export async function onRequestGet({ env }) {
  const paste = await env.variables.get('paste');
  return new Response(getHTML(paste), {
    headers: { 'Content-Type': 'text/html' },
  });
}
