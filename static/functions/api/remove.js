export async function onRequestPost(context) {
  const formData = await context.request.formData();
  const res = await fetch("https://proxy.kaustavmahata.workers.dev/api/remove", {
    method: "POST",
    body: formData,
    headers: {
      "X-Auth-Key": context.env.AUTH_KEY,
    },
  });

  const headers = new Headers(res.headers);

  return new Response(res.body, {
    status: res.status,
    statusText: res.statusText,
    headers,
  });
}

