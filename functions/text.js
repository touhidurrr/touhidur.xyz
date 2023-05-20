const getHTML = (paste) => `<!DOCTYPE html>
<html>
  <head>
    <title>See your Paste!</title>
    <meta name="viewport" content="width=device-width">
  </head>
  <body align="center">
    <textarea id="text" rows="12" cols="40">${paste}</textarea>
    <br><br>
    <button onclick="copy()">Copy to Clipboard!</button>
    <script>
      const text = document.getElementById('text');
      function copy() {
        navigator.clipboard.writeText(text.value);
      }
    </script>
  </body>
</html>`;

export async function onRequestGet({ env }) {
  const paste = await env.variables.get('paste');
  return new Response(getHTML(paste), {
    headers: { 'Content-Type': 'text/html' },
  });
}
