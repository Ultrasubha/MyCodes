/*
 * var other : GameObject;
    other.renderer.material.color.a = 0.5; // 50 % transparent
    other.renderer.material.color.a = 1.0; // fully opaque

    if (raycastHit.collider != null)
        {}

    var raycastHit = Physics2D.Raycast(foot.position, foot.forward, maxDistance, layerMask);
        Debug.DrawRay(foot.position, foot.forward * maxDistance, Color.red);

    [Unity page]
    
    Component[] renderers = GameObject.GetComponentsInChildren(typeof(Renderer));
        foreach (Renderer curRenderer in renderers)
        {
            Color color;
            foreach (Material material in curRenderer.materials)
            {
                color = material.color;
                // change alfa for transparency
                color.a -= 0.01f;
                if (color.a < 0)
                {
                    color.a = 0;                   
                }
                material.color = color;
            }
        }
 
     */