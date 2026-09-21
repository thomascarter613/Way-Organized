"use client";

import { useState } from "react";
import Link from "next/link";
import { createClient } from "@/lib/supabase/client";

export default function SignInPage() {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  async function signIn(event: React.FormEvent) {
    event.preventDefault();
    const supabase = createClient();
    if (!supabase) {
      setMessage("Supabase is not configured yet. Use the demo community link below.");
      return;
    }
    const { error } = await supabase.auth.signInWithOtp({
      email,
      options: { emailRedirectTo: `${window.location.origin}/auth/callback` },
    });
    setMessage(error ? error.message : "Check your email for a secure sign-in link.");
  }

  return <main className="authPage"><div className="authCard"><Link className="brand" href="/"><span className="brandMark">◌</span>Community Platform</Link><div><span className="eyebrow">Welcome</span><h1>Sign in to your community.</h1><p>Use a magic link. Password and social login can be enabled later without changing the account model.</p></div><form onSubmit={signIn} className="authForm"><label htmlFor="email">Email address</label><input id="email" type="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="you@example.com"/><button className="button" type="submit">Email me a sign-in link</button></form>{message && <p className="formMessage" role="status">{message}</p>}<div className="demoBox"><strong>Foundation preview</strong><span>Authentication works after Supabase environment variables are added.</span><Link href="/app">Open demo member area →</Link></div></div></main>;
}
