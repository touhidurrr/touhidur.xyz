export async function onRequestGet(c) {
  return new Response(await variables.get('paste'), {
    headers: { 'Content-Type': 'text/plain' },
  });
}
