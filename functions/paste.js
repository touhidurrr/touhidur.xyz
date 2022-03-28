export async function onRequestPost({ env, request }) {
  await env.variables.put('paste', await request.text());
  return new Response('OK');
}
