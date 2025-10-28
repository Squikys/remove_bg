export async function onRequestPost(context) {
  const formData = await context.request.formData();

  const response = await fetch("https://proxy.kaustavmahata.workers.dev/api/remove", {
    method: "POST",
    body: formData,
    headers: {
      "X-Auth-Key": context.env.AUTH_KEY,
    },
  });

  return new Response(response.body, response);
}
