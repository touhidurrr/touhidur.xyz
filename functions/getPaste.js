export async function onRequestGet() {
  return new Response(await variables.get('paste'), {
    headers: { 'Content-Type': 'text/plain' },
  });
}
