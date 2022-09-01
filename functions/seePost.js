export async function onRequestGet({ env }) {
  return new Response(await env.variables.get('testPost'), {
    headers: { 'Content-Type': 'text/plain' },
  });
}
