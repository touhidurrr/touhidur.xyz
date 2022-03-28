export async function onRequestPost(context) {
  await variables.put('paste', await context.request.text());
  return new Response('OK');
}
