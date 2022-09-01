export async function onRequestPost({ env, request }) {
  let body = await request.text();
  if (body.startsWith('{')) {
    body = JSON.stringify(JSON.parse(body), null, 2);
  }
  await env.variables.put('testPost', body);
  return new Response('OK');
}
