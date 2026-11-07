---
name: react-doctor
description: Diagnoses and fixes React application health issues including unnecessary re-renders, missing memoization, bundle size problems, accessibility violations, and React/MobX anti-patterns. Use PROACTIVELY when a component feels slow, has complex state, or before code review.
---

# React Doctor 🩺

Analyze and optimize React + TypeScript applications. Diagnoses performance bottlenecks, anti-patterns, accessibility issues, and MobX integration problems specific to this project's stack (React 18+, Vite, TailwindCSS v4, Shadcn, MobX).

## Use this skill when
- A component is re-rendering more than expected
- MobX observer pattern is not working correctly
- Bundle size is growing uncontrollably
- Data table or chart is slow with large datasets
- Forms have validation performance issues
- Accessibility audit is needed (WCAG 2.1 AA)
- Code review of a new component before merge

## Do not use this skill when
- The issue is clearly a backend/API problem
- You need design guidance (use ui-ux-pro-max-skill instead)
- The performance issue is in Flutter (use flutter-expert instead)

## Instructions
1. Identify the symptom (slow render, wrong state, missing a11y).
2. Trace the component tree to find the root cause.
3. Apply the minimum change to fix the issue.
4. Verify with React DevTools Profiler approach.
5. Document the fix in a code comment if non-obvious.

---

## Diagnostic Checklist

### 1. Unnecessary Re-renders
```tsx
// ❌ Problem: observer on parent causes all children to re-render
const TeamOverviewPage = observer(() => {
  return <div>{store.athletes.map(a => <AthleteCard athlete={a} />)}</div>
})

// ✅ Fix: make each child an observer independently
const AthleteCard = observer(({ athlete }: { athlete: Athlete }) => (
  <div>{athlete.name} — ACWR: {athlete.acwr}</div>
))
```

### 2. Missing Memoization
```tsx
// ❌ Problem: new function reference on every render
<DataTable
  columns={columns}  
  onRowClick={(row) => navigate(`/athletes/${row.id}`)}  // new ref each render!
/>

// ✅ Fix: useCallback
const handleRowClick = useCallback(
  (row: AthleteRow) => navigate(`/athletes/${row.id}`),
  [navigate]
)
<DataTable columns={columns} onRowClick={handleRowClick} />
```

### 3. MobX Anti-patterns
```tsx
// ❌ Problem: Destructuring breaks reactivity
const { athletes } = athleteStore  // loses MobX tracking!

// ✅ Fix: Access inside observer render
const TeamPage = observer(() => {
  return <div>{athleteStore.athletes.map(...)}</div>  // tracked ✓
})

// ❌ Problem: Mutation outside action
athleteStore.athletes.push(newAthlete)  // MobX strict mode violation

// ✅ Fix: Always use actions
runInAction(() => {
  athleteStore.athletes.push(newAthlete)
})
```

### 4. Bundle Size Audit
```bash
# Analyze bundle
npx vite-bundle-visualizer

# Check for large imports
# ❌ Bad: imports entire library
import _ from 'lodash'

# ✅ Good: tree-shakeable import
import { debounce } from 'lodash-es'
```

### 5. TailwindCSS v4 Anti-patterns
```tsx
// ❌ Problem: @apply with custom classes breaks at build
// In CSS: .my-card { @apply border-border bg-background; }  ← BREAKS

// ✅ Fix: Use CSS variables directly
// In CSS: .my-card { border-color: hsl(var(--border)); background: hsl(var(--background)); }

// ✅ Or inline with Tailwind utilities directly in className
<div className="border border-border bg-background" />
```

### 6. Accessibility (WCAG 2.1 AA)
```tsx
// ❌ Missing: No label on icon button
<button onClick={handleDelete}>
  <Trash2 className="h-4 w-4" />
</button>

// ✅ Fixed: aria-label for screen readers
<button 
  onClick={handleDelete}
  aria-label="Eliminar ejercicio"
  data-el-name="btn-delete-exercise"
>
  <Trash2 className="h-4 w-4" aria-hidden="true" />
</button>
```

### 7. data-el-name Audit
```tsx
// Every interactive element MUST have data-el-name
// Format: [type]-[action]-[entity]

// ✅ Correct patterns:
data-el-name="btn-create-exercise"
data-el-name="input-weight-athlete"
data-el-name="select-discipline-athlete"
data-el-name="table-list-athletes"
data-el-name="badge-acwr-status"
data-el-name="dialog-confirm-delete"
data-el-name="form-daily-readiness"
```

### 8. React Query + MobX Coexistence
```tsx
// Pattern: React Query for server state, MobX for UI state
const TeamOverviewPage = observer(() => {
  // ✅ Server state: React Query
  const { data: athletes, isLoading } = useQuery({
    queryKey: ['team', coachId],
    queryFn: () => athleteService.getTeam(coachId),
    staleTime: 30_000,
  })
  
  // ✅ UI state: MobX
  const { selectedFilter } = uiStore
  
  // ✅ Sync to MobX if needed for cross-component access
  useEffect(() => {
    if (athletes) {
      runInAction(() => { athleteStore.teamData = athletes })
    }
  }, [athletes])
})
```

---

## Prompt Templates

```
# RE-RENDER DIAGNOSIS
"[react-doctor]
El componente [NombreComponente] en [path] está re-renderizando demasiado.
Síntoma: [descripción del comportamiento]
Stack: React 18 + MobX + React Query
Analiza y propón fix mínimo."

# BUNDLE AUDIT
"[react-doctor]
Analiza el bundle del frontend en apps/frontend/
Identifica los 5 imports más pesados y propón alternativas tree-shakeable
Output: tabla con imports + tamaño estimado + alternativa recomendada"

# A11Y AUDIT  
"[react-doctor]
Audita accesibilidad WCAG 2.1 AA del componente [NombreComponente]
Verifica: aria-labels, keyboard navigation, focus states, color contrast
Prioriza por impacto en usuarios con discapacidad visual"

# MOBX REVIEW
"[react-doctor]
Revisa el store [NombreStore].ts en stores/
Verifica: actions correctas, computed correctos, sin mutaciones directas
¿Hay derivaciones computadas que podrían ser computed en vez de state?"
```
