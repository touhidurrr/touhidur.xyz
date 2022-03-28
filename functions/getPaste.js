export async function onRequestGet({ env }) {
  return new Response(await env.variables.get('paste'), {
    headers: { 'Content-Type': 'text/plain' },
  });
}
